import subprocess
import pty
import os
import select
import fcntl
import termios
import array

def my_secure_pty(argv):
    try:
        # Create a pseudo-terminal
        master, slave = pty.openpty()
        
        # Set terminal size
        buf = array.array('H', [24, 80, 0, 0])
        fcntl.ioctl(slave, termios.TIOCSWINSZ, buf)
        
        # Start the process
        process = subprocess.Popen(
            argv,
            stdin=slave,
            stdout=slave,
            stderr=slave,
            preexec_fn=os.setsid,  # Create new process group
            close_fds=True
        )
        
        os.close(slave)  # Close slave fd after passing to subprocess
        
        output = b''
        while True:
            try:
                r, w, e = select.select([master], [], [], 0.1)
                if master in r:
                    data = os.read(master, 4096)
                    if not data:
                        break
                    output += data
                    
                if process.poll() is not None:
                    break
            except OSError:
                break
                
        process.wait()
        os.close(master)
        return output
        
    except Exception as e:
        print(f"Error: {e}")
        return b''

def my_pty_spawn(argv):
    # Open a new pseudo-terminal pair
    master_fd, slave_fd = pty.openpty()

    # Fork the process
    pid = os.fork()
    if pid == 0:  # This is the child process
        # Close the master end
        os.close(master_fd)
        
        # Replace the child's standard file descriptors
        os.dup2(slave_fd, 0) # stdin
        os.dup2(slave_fd, 1) # stdout
        os.dup2(slave_fd, 2) # stderr
        
        # Execute the command
        os.execvp(argv[0], argv)
    else:  # This is the parent process
        # Close the slave end
        os.close(slave_fd)
        
        # Larger buffer size for reading
        BUFFER_SIZE = 4096 
        output = b''
        
        while True:
            r, w, e = select.select([master_fd], [], [])
            if master_fd in r:
                try:
                    data = os.read(master_fd, BUFFER_SIZE)
                    if not data:
                        break # EOF
                    output += data
                except OSError:
                    break
        
        os.waitpid(pid, 0)
        os.close(master_fd)
        return output

def vessel_login_old(self, aws_profile: str) -> None:
    ecr = ECRHandler(aws_profile)
    auth = ecr.generate_auth()

    login_cmd = [ self.vessel or "vessel", "login", auth['registry'], "--username", auth['username'], "--password-stdin"]

    if not auth['password'].endswith('\n'):
      auth['password'] += '\n'

    def master_read(fd):
      try:
        data = os.read(fd, 1024)
      except OSError:
        return b''
      if not data:
        return b''
      text = data.decode(errors='replace')
      logging.info(text)
      # echo output to parent stdout (useful for debugging)
      os.write(1, data)
      # if a password prompt is detected, send the password
      # if 'password' in text.lower() or 'passphrase' in text.lower():
      os.write(fd, auth['password'].encode())
      logging.info(data)
      return data

    try:
      pty.spawn(login_cmd, master_read)
    except Exception as exc:
      logging.error(f"Interactive vessel login failed: {exc}")

def vessel_login_primitive(self, aws_profile: str) -> None:
    ecr = ECRHandler(aws_profile)
    auth = ecr.generate_auth()

    login_cmd = [ self.vessel or "vessel", "login", auth['registry'], "--username", auth['username'], "--password-stdin", "--debug"]

    if not auth['password'].endswith('\n'):
      auth['password'] += '\n'

    # Fork a pseudo-terminal
    pid, fd = pty.fork()

    if pid == 0:
      # Child process (Replace with Vessel Login)
      os.execvp(login_cmd[0], login_cmd)
    else:
      try:
        os.write(fd, auth['password'].encode())
      except OSError as exc:
        logging.error(f"Failed to write password to PTY: {exc}")
        return

      # Read Output
      while True:
        try:
          output = os.read(fd, 1024)
          if not output:
            break
          logging.info(output.decode(errors='replace'))
        except OSError:
          break

# Example usage with a larger read buffer
output = my_pty_spawn(['echo', 'A' * 3000])
print(output.decode())