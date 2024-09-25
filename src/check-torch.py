import torch
import time

print("TORCH_CHECK_STEP 1: VERIFY GPU SUPPORT IN TORCH")
# Check if CUDA is available
print("Is CUDA available: ", torch.cuda.is_available())

# Check the number of GPUs detected
print("Number of GPUs available: ", torch.cuda.device_count())

# Get the name of the current GPU (if any)
if torch.cuda.is_available():
    print("Current GPU device name:", torch.cuda.get_device_name(0))
else:
    print("No GPU detected.")
    raise Exception("No GPU detected.")

print("TORCH_CHECK_STEP 2: RUN SIMPLE TENSOR ON GPU")

def run_simple_model(device_name):
    assert device_name in ['cuda', 'cpu']
    device = torch.device(device_name)
    # Perform a simple computation on the GPU
    a = torch.rand(10000, 10000, device=device)
    b = torch.rand(10000, 10000, device=device)

    start_time = time.time()
    c = torch.matmul(a, b)
    computation_time = time.time() - start_time

    print(f"DEVICE[{device_name}] === Computation time: {computation_time}")
    return computation_time

gpu_time = run_simple_model('cuda')
cpu_time = run_simple_model('cpu')

assert gpu_time < cpu_time, f"GPU computation time ({gpu_time}) should be lower than CPU time ({cpu_time})"

print("TORCH_CHECK_STEP 2: PASSED\n")


print("TORCH_CHECK_STEP 3: Can we move tensors between CPU and GPU?")
# Create a tensor on CPU
tensor_cpu = torch.rand(3, 3, device='cpu')

# Move tensor to GPU
tensor_gpu = tensor_cpu.to('cuda')
print("Tensor successfully moved to GPU")

print ("\n\n====================================")
print("FINISHED TESTS! TORCH configuration seems to be ok!")

