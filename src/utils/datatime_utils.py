from datetime import datetime, time, date

def split_datetime(value: str) -> tuple[date, time]:
    if not value or not value.strip():
        raise ValueError("La fecha de agenda viene vacia")
    
    try:
        dt = datetime.strptime(value.strip(), "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        raise ValueError(f"Formato de fecha invalido: {value!r}") from e
    
    return dt.date(), dt.time()