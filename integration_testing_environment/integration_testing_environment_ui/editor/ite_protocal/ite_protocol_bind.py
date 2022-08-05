def ite_set_protocol(ite_instance):
    # close event
    ite_instance.main_window.protocol("WM_DELETE_WINDOW", ite_instance.ite_close_event)
