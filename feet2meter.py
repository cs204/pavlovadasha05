def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")


def feet2meter(v):
    if 'ft' in v:
      v=v[:-2]
      return float(v)/3.281


main()
