from selenium.webdriver.common.by import By


class TestLocators:
    #Главная страница
    HEADER_PAGE = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' #Заголовок страницы
    '//p[text()="Конструктор"]' #Кнопка "Конструктор"
    '//p[text()="Лента Заказов"]' #Кнопка "Лента заказов"
    BUTTON_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]' #Кнопка "Личный кабинет"
    BUTTON_ENTER_IN_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]' #Кнопка "Войти в аккаунт"
    BUTTON_COLLECT_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'

    '//h1[text()="Соберите бургер"]' #Заголовок таблицы "Соберите бургер"

    '//span[text()="Булки"]' #Выбор категории "Булки" в форме выбора ингредиентов
    '//p[text()="Флюоресцентная булка R2-D3"]' #Выбор булки "Флюоресцентная булка"
    '//p[text()="Краторная булка N-200i"]' #Выбор булки "Краторная булка"

    '//span[text()="Соусы"]' #Выбор категории "Соус"
    '//p[text()="Соус Spicy-X"]' #Выбор соуса "Соус Spicy-X"
    '//p[text()="Соус фирменный Space Sauce"]' #Выбор соуса "фирменный Space Sauce"
    '//p[text()="Соус традиционный галактический"]' #Выбор соуса "традиционный галактический"
    '//p[text()="Соус с шипами Антарианского плоскоходца"]' #Выбор соуса "Соус с шипами Антарианского плоскоходца"

    '//span[text()="Начинки"]'#Выбор категории "Начинки"
    '//p[text()="Мясо бессмертных моллюсков Protostomia"]'
    '//p[text()="Говяжий метеорит (отбивная)"]'
    '//p[text()="Биокотлета из марсианской Магнолии"]'
    '//p[text()="Филе Люминесцентного тетраодонтимформа"]'
    '//p[text()="Хрустящие минеральные кольца"]'
    '//p[text()="Плоды Фалленианского дерева"]'
    '//p[text()="Кристаллы марсианских альфа-сахаридов"]'
    '//p[text()="Мини-салат Экзо-Плантаго"]'
    '//p[text()="Сыр с астероидной плесенью"]'

    '//ul[@class="BurgerConstructor_basket__list__l9dp_"]'#Таблица сбора бургера

    #Окно логина
    LOGIN_HEADER_PAGE = By.XPATH, '//h2[text()="Вход"]' #заголовок окна авторизации
    INPUT_LOGIN = By.XPATH, '//input[@name="name"]' #поле для ввода логина
    INPUT_PASSWORD = By.XPATH, '//input[@name="Пароль"]' #поле для ввода пароля
    BUTTON_ENTER = By.XPATH, '//button[text()="Войти"]' #кнопка "войти"
    LINK_FOR_REGISTRATION = By.XPATH, '//a[text()="Зарегистрироваться"]' #ссылка на регистрацию
    LINK_FOR_RECOVERY = By.XPATH, '//a[text()="Восстановить пароль"]' #ссылка на восстановление пароля

    #Окно регистрации
    REGISTRATION_HEADER = By.XPATH, '//h2[text()="Регистрация"]'
    INPUT_NEW_NAME = By.XPATH, '//div[contains(label, "Имя")]/input' #поле для ввода Имя
    INPUT_NEW_LOGIN = By.XPATH, '//div[contains(label, "Email")]/input' #поле для ввода Email
    INPUT_NEW_PASSWORD = By.XPATH, '//input[@type="password"]' #поле для ввода пароля
    BUTTON_REGISTRATION = By.XPATH, '//button[text()="Зарегистрироваться"]' #кнопка "Зарегистрироваться"
    LINK_FOR_ENTER = By.XPATH, '//a[text()="Войти"]' #ссылка на вход
    ERROR_PASSWORD = By.XPATH, '//p[text()="Некорректный пароль"]'
    ERROR_USER = By.XPATH, '//p[text()="Такой пользователь уже существует"]'

    #Личный кабинет
    LINK_FOR_PROFILE = By.XPATH, '//a[text()="Профиль"]'
    INPUT_ACCOUNT_NAME = By.XPATH, '//div[contains(label, "Имя")]/input' #поле для ввода Имя
    INPUT_ACCOUNT_LOGIN = By.XPATH, '//div[contains(label, "Логин")]/input'

    #Страница востановления пароля
    '//h2[text()="Восстановление пароля"]'
    '//input[@name="name"]' #поле для ввода Email
    '//button[text()="Восстановить"]' #кнопка "Восстановить"
    '//a[text()="Войти"]' #ссылка на вход