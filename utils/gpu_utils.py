import GPUtil
import pyopencl as cl

def get_gpu_info():
    """Fetch GPU information."""
    gpu_text = ""

    # Dedicated GPU (if available)
    gpus = GPUtil.getGPUs()
    if gpus:
        for gpu in gpus:
            gpu_text += f"Dedicated GPU: {gpu.name} ({gpu.load * 100:.1f}% load)\n"
            gpu_text += f"Memory: {gpu.memoryUsed:.1f}MB / {gpu.memoryTotal:.1f}MB\n"
    else:
        gpu_text += "No dedicated GPU detected.\n"

    # Integrated GPU (if available)
    try:
        platforms = cl.get_platforms()
        for platform in platforms:
            for device in platform.get_devices():
                gpu_text += f"Integrated GPU: {device.name} ({device.vendor})\n"
                gpu_text += f"Memory: {device.global_mem_size / (1024**2):.1f} MB\n"
    except Exception:
        gpu_text += "No integrated GPU detected or OpenCL not available.\n"

    return gpu_text