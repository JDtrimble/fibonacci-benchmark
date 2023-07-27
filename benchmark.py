import subprocess
import time
import sys

class UnknownPlatformError(Exception):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"If you have encountered this exception, you are using an OS that is not supported.\nYou are using {sys.platform}"

input_str = "47"
output_str = "2971215073"

def benchmark_python():
    if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
        cmd = ['python3', './src/fib.py']
    elif sys.platform.startswith("win"):
        cmd = ['python', '.\\src\\fib.py']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_cpp():
    if sys.platform.startswith("linux"):
        cmd = ['./build/cpp(linux)']
    elif sys.platform.startswith("win"):
        cmd = ['.\\build\\cpp(win)']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_rust():
    if sys.platform.startswith("linux"):
        cmd = ['./build/rust(linux)']
    elif sys.platform.startswith("win"):
        cmd = ['.\\build\\rust(win)']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_c():
    if sys.platform.startswith("linux"):
        cmd = ['./build/c(linux)']
    elif sys.platform.startswith("win"):
        cmd = ['.\\build\\c(win)']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_pascal():
    if sys.platform.startswith("linux"):
        cmd = ['./build/pascal(linux)']
    elif sys.platform.startswith("win"):
        cmd = ['.\\build\\pascal(win)']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_java():
    if sys.platform.startswith("linux") or sys.platform.startswith("win"):
        cmd = ['java', './src/fib.java']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution

def benchmark_ruby():
    if sys.platform.startswith("linux") or sys.platform.startswith("win"):
        cmd = ['ruby', './src/fib.rb']
    else:
        raise UnknownPlatformError
    start = time.time()
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=input_str)
    end = time.time()
    time_of_execution = end - start
    return output.strip(), time_of_execution


if __name__ == "__main__":
    with open('task.txt', 'r') as task_file:
        line = task_file.readline().strip()
        print(line)
    input_str = input(f"Input:\t").strip()

    lang = {}
    lang['python'] = benchmark_python()
    lang['c'] = benchmark_c()
    lang['cpp'] = benchmark_cpp()
    lang['rust'] = benchmark_rust()
    lang['pascal'] = benchmark_pascal()
    lang['java'] = benchmark_java()
    lang['ruby'] = benchmark_ruby()
    
    sorted_results = sorted(lang.items(), key=lambda item: item[1][1], reverse=True)
    
    for lang_name, (output, execution_time) in sorted_results:
        print(f"{lang_name.capitalize()} time: \t{execution_time:.6f} seconds")

    for lang_name, (output, execution_time) in sorted_results:    
        print(f"{lang_name.capitalize()} output:\t{output}")
