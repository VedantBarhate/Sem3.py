# bucket list Q9

# Implement a Singleton class Configuration that reads configuration settings from a file.
# Ensure only one instance of Configuration exists and is used throughout the application.
# Add a method get_setting to retrieve configuration values.
# Demonstrate accessing configuration settings.
# Concepts Covered: Singleton Pattern with Configuration

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Configuration:
    def __init__(self, config_file):
        self.config = open(config_file, 'r')

    def get_setting(self):
        return self.config.read()

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    config1 = Configuration('settings.txt')
    config2 = Configuration('settings.txt')

    print(config1 is config2)

    setting = config1.get_setting()
    print(setting)