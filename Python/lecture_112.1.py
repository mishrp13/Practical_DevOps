from pathlib import Path
from typing import list, Union


def archive_log_files(log_directory: Union[str,Path], archive_date: str)-> list[Path]:


    if not isinstance(log_directory,(str,Path)):
        raise TypeError("log_directory must be a string or a path object")
    
    log_dir_path= Path(log_directory)

    if not log_dir_path.is_dir():
        raise ValueError(f" Directory does not exist or is not a directory: {log_dir_path}")
    
    if not isinstance(archive_date,str):
        raise TypeError("archive date must be a string")
    
    parts= archive_date.split('-')

    is_valid_format = (
        len(parts)==3 and
        len(parts[0])==4 and parts[0].isdigit() and
        len(parts[1])==2 and parts[1].isdigit() and
        len(parts[2])==2 and parts[2].isdigit()
    )

    if not is_valid_format:
        raise ValueError("archive date must be in YYYY-MM-DD format")
    
    renamed_files= []

    for item in log_dir_path.iterdir():
        if item.is_file() and item.suffix == ".log":
            new_stem= f"{item.stem}-{archive_date}"
            new_path=item.with_stem(new_stem)
            item.rename( new_path)
            renamed_files.append(new_path)

    return renamed_files


if __name__ == "__main__":
    result =archive_log_files(
        "test_logs",
        "2026-05-20"
    )

print(result)

