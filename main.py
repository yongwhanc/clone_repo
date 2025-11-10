implemented = []
module_list = ["A", "B", "conflict", "is_it_okay"]
for module_name in module_list:
    try:
        module = __import__(module_name)
        if hasattr(module, "run"):
            module.run()
            implemented.append(module_name)
    except ImportError:
        print(f"Skipped {module_name} (module is not implemented yet)")

if len(implemented) == len(module_list):
    print("All modules are implemented!!")
else:
    for module_name in module_list:
        if module_name not in implemented:
            print(f"Module {module_name} is not implemented yet.")