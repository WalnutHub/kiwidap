
import lvgl as lv
import usys as sys

import kiwidap_ui
from kiwidap_ui import kiwidap_ui,base_page,btn_style,bar_style
import kiwidap_api


class targetreg_page(base_page):
    def __init__(self):
        super().__init__()

    def ui(self):
        ##################### Connect Button #########################
        table_style = btn_style(self.themes[self.current_theme]["btn1_bg_color"],10)
        table = lv.table(self)
        table.add_style(table_style, lv.PART.MAIN)
        table.add_style(table_style, lv.PART.ITEMS)
        table.set_cell_value(0,0,"Reg")
        table.set_cell_value(0,1,"Value")
#        table.set_col_width(0,80)
#        table.set_col_width(1,80)
        table.set_size(180,163)
        table.align(lv.ALIGN.TOP_MID, 0, 80)

        targetreg_label = lv.label(self)
#        targetreg_label.set_recolor(True)
        targetreg_label.set_style_text_font(self.font_24, 0)
        targetreg_label.set_text("#87de87 TARGET@REG")
        targetreg_label.align(lv.ALIGN.TOP_MID, 0, 30)



def test():
    app = kiwidap_ui()
    targetreg_page_instance = targetreg_page()
    targetreg_page_instance.ui()
    app.add_page(targetreg_page_instance)
    app.start()
    while True:
        pass

#test()
