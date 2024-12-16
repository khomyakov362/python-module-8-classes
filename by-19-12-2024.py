class PowerSupply:

    def __init__(self, power):
        self.power = power
        
    def apply_voltage(self, voltage):
        print(f'{voltage} volts is applied to the PSU.')
    
class Motherboard:

    def __init__(self, chipset):
        self.chipset = chipset
    
    def allocate_voltage(self, voltage):
        print(f'{voltage} volts is allocated to the components.')

class CPU:

    def __init__(self, processor_frequency, number_of_cores):
        self.processor_frequency = processor_frequency
        self.number_of_cores = number_of_cores
    
    def turn_on_turbo_mode(self):
        print(f'The Turbo Mode is activated all the {self.number_of_cores} are working to full power')
    
class RAM:

    def __init__(self, ram_frequency, ram_size):
        self.ram_frequency = ram_frequency
        self.ram_size = ram_size
    
    def store_data(self, data):
        print(f'The data is stored in RAM')
    
    def get_data(self, memory_address):
        print(f'The data from memory address {memory_address} is returned')

class SSD:

    def __init__(self, SSD_size):
        self.SSD_size = SSD_size
    
    def save_data(self, data):
        print('The data is saved on the SSD')

    def remove_data(self, data):
        print('The data is deleted.')

class GraphicsCard:

    def __init__(self, graphics_card_model, graphics_card_memory):
        self.graphics_card_model = graphics_card_model
        self.graphics_card_memory = graphics_card_memory

    def display_graphics(self, graphics):
        print('The graphics is displayed')

class PC_inheritance(PowerSupply, Motherboard, CPU, RAM, SSD, GraphicsCard):

    def __init__(self, power, chipset, processor_frequency, number_of_cores, ram_frequency, ram_size, ssd_size, graphics_card_model, graphics_card_memory):
        PowerSupply.__init__(self, power)
        Motherboard.__init__(self, chipset)
        CPU.__init__(self, processor_frequency, number_of_cores)
        RAM.__init__(self, ram_frequency, ram_size)
        SSD.__init__(self, ssd_size)
        GraphicsCard.__init__(self, graphics_card_model, graphics_card_memory)

pc_inherited = PC_inheritance(10, 'H610', 3, 4, 5, 16, 400, 'NVIDIA', 8)

pc_inherited.apply_voltage(220)
print(pc_inherited.graphics_card_memory)
        
class PC_composition:

    def __init__(self, power, chipset, processor_frequency, number_of_cores, ram_frequency, ram_size, ssd_size, graphics_card_model, graphics_card_memory):
        self.power_supply = PowerSupply(power)
        self.mother_board = Motherboard(chipset)
        self.CPU = CPU(processor_frequency, number_of_cores)
        self.RAM = RAM(ram_frequency, ram_size)
        self.SSD = SSD(ssd_size)
        self.grapics_card = GraphicsCard(graphics_card_model, graphics_card_memory)

pc_composed = PC_composition(10, 'H610', 3, 4, 5, 16, 400, 'NVIDIA', 8)

pc_composed.power_supply.apply_voltage(220)
pc_composed.CPU.turn_on_turbo_mode()
