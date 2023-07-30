from selenium.webdriver.common.by import By

class TestLocators:
    #Главная страница
    HEADER_BANNER = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]' #Заголовок страницы
    BUTTON_CONSTRUCTOR = By.XPATH, '//p[text()="Конструктор"]' #Кнопка "Конструктор"
    BUTTON_ACCOUNT = By.XPATH, '//p[text()="Личный Кабинет"]' #Кнопка "Личный кабинет"
    BUTTON_ENTER_IN_ACCOUNT = By.XPATH, '//button[text()="Войти в аккаунт"]' #Кнопка "Войти в аккаунт"
    BUTTON_COLLECT_ORDER = By.XPATH, '//button[text()="Оформить заказ"]'
    TABLE_HEADER = By.XPATH, '//h1[text()="Соберите бургер"]' #Заголовок таблицы "Соберите бургер"
    CHAPTER_BUN = By.XPATH, '//span[text()="Булки"]' #Выбор категории "Булки" в форме выбора ингредиентов
    BUN_FIRST = By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]' #Выбор булки "Флюоресцентная булка"
    CHAPTER_SAUCE = By.XPATH, '//span[text()="Соусы"]' #Выбор категории "Соус"
    SAUCE_FIRST = By.XPATH, '//p[text()="Соус Spicy-X"]' #Выбор соуса "Соус Spicy-X"
    CHAPTER_TOPPING = By.XPATH, '//span[text()="Начинки"]'#Выбор категории "Начинки"
    TOPPING_FIRST = By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]' #Выбор начинки "Мясо бессмертных моллюсков Protostomia"

    #Окно логина
    LOGIN_HEADER_PAGE = By.XPATH, '//h2[text()="Вход"]' #заголовок окна авторизации
    INPUT_LOGIN = By.XPATH, '//input[@name="name"]' #поле для ввода логина
    INPUT_PASSWORD = By.XPATH, '//input[@name="Пароль"]' #поле для ввода пароля
    BUTTON_ENTER = By.XPATH, '//button[text()="Войти"]' #кнопка "войти"
    LINK_FOR_REGISTRATION = By.XPATH, '//a[text()="Зарегистрироваться"]' #ссылка на регистрацию
    LINK_FOR_RECOVERY = By.XPATH, '//a[text()="Восстановить пароль"]' #ссылка на восстановление пароля

    #Окно регистрации
    REGISTRATION_HEADER = By.XPATH, '//h2[text()="Регистрация"]' #Заголовок формы регистрации
    INPUT_NEW_NAME = By.XPATH, '//div[contains(label, "Имя")]/input' #поле для ввода Имя
    INPUT_NEW_LOGIN = By.XPATH, '//div[contains(label, "Email")]/input' #поле для ввода Email
    INPUT_NEW_PASSWORD = By.XPATH, '//input[@type="password"]' #поле для ввода пароля
    BUTTON_REGISTRATION = By.XPATH, '//button[text()="Зарегистрироваться"]' #кнопка "Зарегистрироваться"
    LINK_FOR_ENTER = By.XPATH, '//a[text()="Войти"]' #ссылка на вход
    ERROR_PASSWORD = By.XPATH, '//p[text()="Некорректный пароль"]' # Ошибка "Некорректный пароль"
    ERROR_USER = By.XPATH, '//p[text()="Такой пользователь уже существует"]' # Ошибка "пользователь существует"

    #Личный кабинет
    LINK_FOR_PROFILE = By.XPATH, '//a[text()="Профиль"]' #Вкладка "Профиль"
    INPUT_ACCOUNT_NAME = By.XPATH, '//div[contains(label, "Имя")]/input' #поле Имя
    INPUT_ACCOUNT_LOGIN = By.XPATH, '//div[contains(label, "Логин")]/input' #поле Логин
    BUTTON_EXIT = By.XPATH, '//button[text()="Выход"]' #Кнопка "Выход"
