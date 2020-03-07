import pickle
import os

unv_counter = "total_test_counter.pickle"

def save_state(count):
    # Load the count back to pickle
    with open(unv_counter, 'wb') as p_handle:
        pickle.dump(count, p_handle)

def load_state():
    if not os.path.exists(unv_counter):
        count = 0
    else:
        with open(unv_counter, 'rb') as p_handle:
            count = pickle.load(p_handle)
    
    return count

count = load_state()

print("run:", count)
count += 1

save_state(count)