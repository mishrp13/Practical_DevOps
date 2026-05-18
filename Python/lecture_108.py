from pathlib import Path

config_dir= Path(".")
file_name= "settings.yaml"

print(config_dir,type(config_dir))

config_path= config_dir / file_name

print(config_path.resolve())


service_log= Path(".")
print(f"Exists: {service_log.exists}")
print(f"Is a directory? : {service_log.is_dir}")
print(f"Parent: {service_log.parent}")
print(f"Name: {service_log.name}")
print(f"stem: {service_log.stem}")
print(f"suffix: {service_log.suffix}")
print(f"Resolved absolute path: {service_log.resolve()}")