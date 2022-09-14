def most_used_laptops(lap_price):
    most_used_laptops = lap_price.Company.value_counts().reset_index()
    most_used_laptops.rename(columns={'index':'Type of Laptop','Company':'Count of Laptops'}, inplace=True)
    return most_used_laptops

def inches_of_laptops(lap_price):
    laptops_inches = lap_price.Inches.value_counts().reset_index()
    laptops_inches.rename(columns={'index':'inches','Inches':'Count of Laptops'}, inplace=True)
    return laptops_inches

def Screen_Resolution_of_Laptops(lap_price):
    laptops_ScreenResolution = lap_price.ScreenResolution.value_counts().reset_index()
    laptops_ScreenResolution.rename(columns={'index':'Screen Resolution', 'ScreenResolution':'Count of Laptops'}, inplace=True)
    return laptops_ScreenResolution

def CPU(lap_price):
    cpu = lap_price.Cpu.value_counts().reset_index()
    cpu.rename(columns={'index':'Types of CPU', 'Cpu':'Count of Laptops'}, inplace=True)
    return cpu

def Ram(lap_price):
    ram = lap_price.Ram.value_counts().reset_index()
    ram.rename(columns={'index':'Types of Ram', 'Ram':'Count of Laptops'}, inplace=True)
    return ram

def Memory(lap_price):
    memory = lap_price.Memory.value_counts().reset_index()
    memory.rename(columns={'index':'Types of Memory', 'Memory':'Count of Laptops'}, inplace=True)
    return memory

def Gpu(lap_price):
    gpu = lap_price.Gpu.value_counts().reset_index()
    gpu.rename(columns={'index':'Types of Gpu\'s', 'Gpu':'Count of Laptops'}, inplace=True)
    return gpu

def Os(lap_price):
    os = lap_price.OpSys.value_counts().reset_index()
    os.rename(columns={'index':'Types of Operating Systems', 'OpSys':'Count of Laptops'}, inplace=True)
    return os

def Weight(lap_price):
    weight = lap_price.Weight.value_counts().reset_index()
    weight.rename(columns={'index':'Weight', 'Weight':'Count of Laptops'}, inplace=True)
    return weight