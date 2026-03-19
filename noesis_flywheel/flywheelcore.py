import time
from execution import ExecutionEngine # Uses your existing file
from memory.registry import RegistryManager

class NoesisFlywheel:
    def __init__(self):
        self.registry = RegistryManager()
        self.executor = ExecutionEngine()
        self.state = "IDLE"

    def charge_continuity(self, task_complexity):
        """Calculates computational 'pressure' based on your expansion logic."""
        return task_complexity * 1.618 # Golden ratio for recursive scaling

    def spin(self, input_signal):
        print(f"[*] Flywheel Engaged: Processing through Sensory Layer...")
        
        # 1. Sense (Input from your sensory_layer)
        context = self.registry.get_context(input_signal)
        
        # 2. Think (The Noesis Logic)
        pressure = self.charge_continuity(len(input_signal))
        print(f"[!] Current Spatial Pressure: {pressure}")

        # 3. Act (Persistent execution)
        result = self.executor.run_safe(input_signal, context)
        
        # 4. Persist (Log back to evolutionary_log)
        self.registry.log_evolution("flywheel_cycle", result)
        
        return result

if __name__ == "__main__":
    flywheel = NoesisFlywheel()
    while True:
        # Autonomous loop
        flywheel.spin("awaiting_next_evolutionary_step")
        time.sleep(10) 

