from django.db import models


class Cable(models.Model):
    wire_core = models.ForeignKey('WireCore', on_delete=models.CASCADE, verbose_name='Сечение')
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Кабель'
        verbose_name_plural = 'Кабеля'

    def __str__(self):
        return self.name

    def get_fields(self):
        return dict({"wire_core": {"Жила": str(self.wire_core)},
                     "name": {"Название": self.name}})


class Port(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    number = models.CharField(max_length=100, verbose_name='Номер')
    cable = models.ForeignKey('Cable', on_delete=models.CASCADE, verbose_name='Кабель')

    class Meta:
        verbose_name = 'Порт'
        verbose_name_plural = 'Порты'

    def __str__(self):
        return self.name

    def get_fields(self):
        return dict({"name": {"Название": self.name},
                     "number": {"Номер": self.number},
                     "cable": {"Кабель": str(self.cable)}})


class Equipment(models.Model):
    responsible = models.ForeignKey('Responsible', on_delete=models.CASCADE, verbose_name='Ответственный')
    name = models.CharField(max_length=100, verbose_name='Название')
    port = models.ForeignKey('Port', on_delete=models.CASCADE, verbose_name='Порт')

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

    def __str__(self):
        return self.name

    def get_fields(self):
        return dict({"responsible": {"Ответственный", str(self.responsible)},
                     "name": {"Название": self.name},
                     "port": {"Порт": str(self.port)}})


class WireCore(models.Model):
    content = models.CharField(max_length=100, verbose_name='Содержимое')

    class Meta:
        verbose_name = 'Жила'
        verbose_name_plural = 'Жилы'

    def __str__(self):
        return self.content

    def get_fields(self):
        return dict({"content": {"Содержимое": self.content}})


class Responsible(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    subdivision = models.ForeignKey('Subdivision', on_delete=models.CASCADE, verbose_name='Подразделение')

    class Meta:
        verbose_name = 'Ответственный'
        verbose_name_plural = 'Ответственные'

    def __str__(self):
        return self.full_name

    def get_fields(self):
        return dict({"full_name": {"ФИО": self.full_name},
                     "subdivision": {"Подразделение": str(self.subdivision)}})


class Subdivision(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name='Организация')
    leader = models.CharField(max_length=150, verbose_name='Руководитель')

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return self.name

    def get_fields(self):
        return dict({"name": {"Название": self.name},
                     "organization": {"Организация": str(self.organization)},
                     "leader": {"Руководитель": self.leader}})


class Organization(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name='Владелец')
    phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    room = models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name='Помещение')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.owner.full_name

    def get_fields(self):
        return dict({"owner": {"Владелец": str(self.owner)},
                     "phone": {"Номер телефона": self.phone},
                     "room": {"Помощение": str(self.room)}})


class Room(models.Model):
    renter = models.CharField(max_length=100, verbose_name='Арендатор')
    building = models.ForeignKey('Building', on_delete=models.CASCADE, verbose_name='Здание')
    number = models.CharField(max_length=100, verbose_name='Номер')

    class Meta:
        verbose_name = 'Помещение'
        verbose_name_plural = 'Помещения'

    def __str__(self):
        return self.number

    def get_fields(self):
        return dict({"renter": {"Арендатор": self.renter},
                     "building": {"Здание": str(self.building)},
                     "number": {"Номер": self.number}})


class Building(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, verbose_name='Владелец')
    address = models.CharField(max_length=100, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'

    def __str__(self):
        return self.address

    def get_fields(self):
        return dict({"owner": {"Владелец": str(self.owner)},
                     "address": {"Адрес": self.address}})


class Owner(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='ФИО')

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

    def __str__(self):
        return self.full_name

    def get_fields(self):
        return dict({"full_name": {"ФИО": self.full_name}})
