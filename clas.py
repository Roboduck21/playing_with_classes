class HardDrive:

    def __init__(self, name, storage_capacity, drive_type):
        self.name = name
        self.storage_capacity = storage_capacity
        self.drive_type = drive_type

    def space_available(self):
        print("There is {}GB of space available on this drive. :)".format(self.storage_capacity - 25))
