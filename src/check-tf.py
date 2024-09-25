import tensorflow as tf

print("TF_CHECK_STEP 1: VERIFY GPU SUPPORT IN TF")
print("TensorFlow version:", tf.__version__)
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

gpus = tf.config.list_physical_devices('GPU')

print("TF_CHECK_STEP 2: TRY TO ALLOCATE MEMORY USING TF ON GPU")
if gpus:
    try:
        # Restrict TensorFlow to only use the first GPU
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')

        # Allocate memory on the GPU
        tf.config.experimental.set_memory_growth(gpus[0], True)
        
        print("TensorFlow is using GPU:", tf.config.list_physical_devices('GPU'))
    except RuntimeError as e:
        raise e
else:
    print("No GPU found")
    raise Exception("No GPU found")


print("TF_CHECK_STEP 3: RUN TEST MODEL and COMPARE times")
import time

def run_simple_model(device_name):
    assert device_name in ['GPU', 'CPU']
    
    start = time.time()
    with tf.device(f"/{device_name}:0"):
        a = tf.random.normal([10000, 10000])
        b = tf.random.normal([10000, 10000])
        c = tf.matmul(a, b)

    computation_time = time.time() - start
    print(f"DEVICE[{device_name}] === Computation time: {computation_time}")
    return computation_time

gpu_time = run_simple_model("GPU")
cpu_time = run_simple_model("CPU")

assert gpu_time < cpu_time, f"GPU computation time ({gpu_time}) should be lower than CPU time ({cpu_time})"

print ("\n\n====================================")
print("FINISHED TESTS! TensorFlow configuration seems to be ok!")

