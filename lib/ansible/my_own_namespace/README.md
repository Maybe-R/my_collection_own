# Домашнее задание Создание собственных модулей
## Предварительная настройка
<img width="2415" height="1541" alt="image" src="https://github.com/user-attachments/assets/02360b79-9dec-41b9-bdb8-1b5039d5e687" />

## Основная часть

Шаг 1. В виртуальном окружении создайте новый my_own_module.py файл.

Шаг 2. Наполните его содержимым - *добавить ссылку в репе*

Шаг 3. Заполните файл в соответствии с требованиями Ansible так, чтобы он выполнял основную задачу: module должен создавать текстовый файл на удалённом хосте по пути, определённом в параметре path, с содержимым, определённым в параметре content.

Шаг 4. Проверьте module на исполняемость локально.

<img width="2520" height="782" alt="image" src="https://github.com/user-attachments/assets/3d4ac6b2-4ff4-4577-b93f-54ba172e0ee5" />

Проверяем созданный файл в дирректории

<img width="1250" height="1063" alt="image" src="https://github.com/user-attachments/assets/7f1c9d26-2ee3-437d-90c7-752028d7855c" />

Шаг 5. Напишите single task playbook и используйте module в нём.

Шаг 6. Проверьте через playbook на идемпотентность.

<img width="2176" height="1436" alt="image" src="https://github.com/user-attachments/assets/cae83d4e-065f-4390-9a80-5d54f7a64725" />

Шаг 10. Single task playbook преобразуйте в single task role и перенесите в collection. У role должны быть default всех параметров module.

Шаг 11. Создайте playbook для использования этой role.

Шаг 16. Запустите playbook, убедитесь, что он работает.

<img width="2505" height="1384" alt="image" src="https://github.com/user-attachments/assets/8294aad9-0a3c-4dc5-bac6-f433a7cd100a" />

Проверяем созданный файл

<img width="2007" height="270" alt="image" src="https://github.com/user-attachments/assets/060a3f51-fa8d-4e2e-a5e2-b6c991fc2f2c" />


