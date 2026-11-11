def avto_info(brand, model, color, gearbox, year, price):
    return {
        "brand": brand,
        "model": model,
        "color": color,
        "gearbox": gearbox,
        "year": year,
        "price": price,
    }


def info_print(avto):
    print(f"Brend: {avto['brand']}")
    print(f"Model: {avto['model']}")
    print(f"Rang: {avto['color']}")
    print(f"Transmission: {avto['gearbox']}")
    print(f"Yil: {avto['year']}")
    print(f"Narx: ${avto['price']:,}")
