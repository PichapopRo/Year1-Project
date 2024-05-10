from Program_UI import *


def main():
    model = PCPartModel()
    controller = PCPartController(model, None)
    view = PCPartView(controller)
    controller.view = view
    view.mainloop()


if __name__ == "__main__":
    main()
