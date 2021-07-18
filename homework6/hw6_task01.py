"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""


def instances_counter(cls: "SomeClass") -> "SomeClass":
    """Decorator that adds instances counter to a class.
    Adds two methods:
    - get_created_instances: returns the number of
    created class instances.
    - reset_instances_counter: resets the instances counter,
    returns the number of instances before reset.
    Returns:
        The same class with added methods.
    """

    initial_init = cls.__init__
    counter = 0

    def new_init(self, *args, **kwargs) -> None:
        nonlocal counter
        counter += 1
        initial_init(self, *args, **kwargs)

    cls.__init__ = new_init

    @classmethod
    def get_created_instances(cls: "SomeClass") -> int:
        return counter

    cls.get_created_instances = get_created_instances

    @classmethod
    def reset_instances_counter(cls: "SomeClass") -> int:
        nonlocal counter
        counter_before_reset_instances = counter
        counter = 0
        return counter_before_reset_instances

    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass
