class AttrDisplay:
    def gatherAttrs(self) -> str:
        attrs = []
        for key in list(self.__dict__.keys()):
            attrs.append('%s=%s' % (key, self.__dict__[key]))
        return ', '.join(attrs)


    def __repr__(self) -> str:
        return '[%s, %s]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':
    class TopClass(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopClass.count
            self.attr2 = TopClass.count + 1
            TopClass.count += 2
    

    class SubClass(TopClass):
        pass


    X = TopClass()
    Y = SubClass()

    print(X)
    print(Y)

    print(SubClass.count)
