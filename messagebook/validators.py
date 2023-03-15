from rest_framework import serializers


class Phonevalidator:

    def __call__(self, value):
        phone_number = str(value)
        if not phone_number.startswith("7"):
            raise serializers.ValidationError("Номер телефона должен начинаться с 7")
        if len(phone_number) != 11:
            raise serializers.ValidationError("Номер телефона должен содержать 11 цифр")
        if not phone_number.isdigit():
            raise serializers.ValidationError("Номер телефона должен содержать только цифры")
        return value


class Passwordvalidator:

    def __call__(self, value):
        import re
        user_password = str(value)

        if len(user_password) < 8:
            raise serializers.ValidationError("Пароль должен быть не менее 8 символов")
        if not re.findall('\d', user_password):
            raise serializers.ValidationError("Пароль должен включать цифры")
        return value


class Emailvalidator:

    def __call__(self, value):
        # email = models.EmailField(_("email address"), blank=True)
        value = value.split('@')[1]
        words = ["mail.ru", "yandex.ru"]
        for word in words:
            if word == value:
                return value
        raise serializers.ValidationError("разрешены домены: mail.ru, yandex.ru")


class Сensorshipvalidator:

    def __call__(self, value):
        title = str(value)
        words = ["ерунда", "глупость", "чепуха"]
        for word in words:
            if word.lower() in value.lower():
                raise serializers.ValidationError("Автор вписал в заголовок запрещенные слова")
        return value

