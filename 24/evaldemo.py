from builderlib import Builder, deco, Descriptor

print('# evaldemo module start')


@deco
class Klass(Builder):
    print('# Klass body')

    attr = Descriptor()

    def __init__(self):
        super().__init__()
        print(f'# Klass.__init__({self!r})')

    def __repr__(self):
        return '<Klass instance>'


def main():
    obj = Klass()
    obj.method_a()
    obj.method_b()
    obj.attr = 999


if __name__ == '__main__':
    main()

print('# evaldemo module end')
