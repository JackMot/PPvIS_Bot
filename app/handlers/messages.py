help_message = 'Для того чтобы отправить ссылку на лабораторную работу, ' \
               'зарегестрируйтесь при помощи команды:' \
               '"/login"\n' \
               'Затем воспользуйтесь командой:' \
               '"/lab"\n' \
               'Если вы являетесь преподователем,воспользуйтесь командой:' \
               '"/work"\n'

start_message = 'Приветствую вас. Это интеллектуальный ассистент по сдачам лабороторных работ.\n' \
                'Для ознакомления со списком команд введите "/help"\n' + help_message

stop_message = 'Работа приостановлена'

cancel_message = 'Действие отменено'

admin_login_message = 'Вы успешно вошли в систему как администратор'

system_welcome_message = 'System mod is successful activated'

system_restart_option_message = 'Do you want to restart the program? [y/n]'

system_stop_option_message = 'Do you want to stop the program? [y/n]'

system_update_option_message = 'Do you want to update the program? [y/n]'

system_restart_message = 'The system will be rebooted shortly'

system_restart_cancel_message = 'Restart aborted'

system_update_message = 'The system will be updated shortly'

system_update_cancel_message = 'Restart aborted'

system_stop_message = 'The system will be stopped shortly'

system_stop_cancel_message = 'Stop aborted'

work_start_message = 'Выберите действие, используя клавиатуру ниже'

login_wrong_input_message = 'Пожалуйста, выберите вариант входа, используя клавиатуру ниже'

link_success_update_message = 'Ссылка успешно добавлена'

link_update_start_message = 'Отправьте ссылку на вашу лабораторную работу'

student_login_message = 'Вы успешно вошли в систему как студент'

lecturer_login_message = 'Вы успешно вошли в систему как преподаватель'

register_start_message = 'Для регистрации в системе нажмите на кнопку "Зарегистрироваться"'

register_missing_data_message = 'Произошла ошибка: ваших данных нет в системе, обратитесь к администратору за помощью'

register_double_registration_message = 'Вы уже зарегистрированы в системе.\nДля того чтобы войти в свою учетную ' \
                                       'запись вы можете воспользоваться командой /login или кнопкой '

error_message = 'Похоже что-то пошло не так...\n' \
                'Попробуйте еще раз '

api_error_message = 'Связть с сервисами гугл в данный момент не установлена\n' \
                'Пожалуйста,попробуйте еще раз позже '
MESSAGES = {
    'start': start_message,
    'stop': stop_message,
    'help': help_message,
    'cancel': cancel_message,
    'admin.login': admin_login_message,
    'system.start': system_welcome_message,
    'system.restart.option': system_restart_option_message,
    'system.stop.option': system_stop_option_message,
    'system.update.option': system_update_option_message,
    'system.restart': system_restart_message,
    'system.restart.cancel': system_restart_cancel_message,
    'system.update': system_update_message,
    'system.update.cancel': system_update_cancel_message,
    'system.stop': system_stop_message,
    'system.stop.cancel': system_stop_cancel_message,
    'work.start': work_start_message,
    'login.error': login_wrong_input_message,
    'link_update': link_success_update_message,
    'link_start': link_update_start_message,
    'error': error_message,
    'api_error': api_error_message,
    'lecturer.login': lecturer_login_message,
    'student.login': student_login_message,
    'register.start': register_start_message,
    'register.data.error': register_missing_data_message,
    'register.double.registration': register_double_registration_message,
}
