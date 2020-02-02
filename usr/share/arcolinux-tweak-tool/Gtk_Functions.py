#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
import Functions
from Functions import os
#====================================================================
#                       GTK FUNCTIONS
#====================================================================
def get_gtk_themes(self, combo):
    if os.path.isfile(Functions.gtk3_settings):
        try:
            active_combo = ""
            combo.get_model().clear()
            coms = []
            with open(Functions.gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(Functions.gtk_get_position(lines, "gtk-theme-name"))
            output = lines[pos].split("=")
            active_combo = output[1].lstrip().rstrip()

            for folder in os.listdir("/usr/share/themes"):
                if os.path.isdir("/usr/share/themes/" + folder):
                    check = os.listdir("/usr/share/themes/" + folder)
                    if "gtk-3.0" in check:
                        coms.append(folder)

            coms.sort()

            for i in range(len(coms)):
                combo.append_text(coms[i])
                if(coms[i] == active_combo):
                    combo.set_active(i)
        except:
            Functions.MessageBox("ERROR!!", "An error has occured getting this setting \'gtk-theme-name\'")

def get_icon_themes(self, combo):
    if os.path.isfile(Functions.gtk3_settings):
        try:
            active_combo_icon = ""
            combo.get_model().clear()
            coms = []
            with open(Functions.gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(Functions.gtk_get_position(lines, "gtk-icon-theme-name"))
            output = lines[pos].split("=")
            active_combo_icon = output[1].lstrip().rstrip()

            for folder in os.listdir("/usr/share/icons"):
                if os.path.isdir("/usr/share/icons/" + folder):
                    check = os.listdir("/usr/share/icons/" + folder)
                    if not "cursors" in check:
                        coms.append(folder)

            coms.sort()

            for i in range(len(coms)):
                combo.append_text(coms[i])
                if(coms[i] == active_combo_icon):
                    combo.set_active(i)
        except:
            Functions.MessageBox("ERROR!!", "An error has occured getting this setting \'gtk-icon-theme-name\'")

def get_cursor_themes(self, combo):
    if os.path.isfile(Functions.gtk3_settings):
        try:
            combo.get_model().clear()
            active_combo_cursor = ""
            coms = []
            with open(Functions.gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(Functions.gtk_get_position(lines, "gtk-cursor-theme-name"))
            output = lines[pos].split("=")
            active_combo_cursor = output[1].lstrip().rstrip()

            for folder in os.listdir("/usr/share/icons"):
                if os.path.isdir("/usr/share/icons/" + folder):
                    check = os.listdir("/usr/share/icons/" + folder)
                    if "cursors" in check:
                        coms.append(folder)

            coms.sort()

            for i in range(len(coms)):
                combo.append_text(coms[i])
                if(coms[i] == active_combo_cursor):
                    combo.set_active(i)
        except:
            Functions.MessageBox("ERROR!!", "An error has occured getting this setting \'gtk-cursor-theme-name\'")


def get_gtk_settings(item):
    if os.path.isfile(Functions.gtk3_settings):
        active_cursor = ""
        try:
            with open(Functions.gtk3_settings, "r") as f:
                lines = f.readlines()
                f.close()
            pos = int(Functions.gtk_get_position(lines, item))
            output = lines[pos].split("=")
            active_cursor = output[1].lstrip().rstrip()

        except:
            Functions.MessageBox("ERROR!!", "An error has occured getting this setting \'get_gtk_settings\'")
            if item == "gtk-cursor-theme-size":
                active_cursor = "24"
        
        return active_cursor

def gtk2_save_settings(value, item):
    if not os.path.isfile(Functions.gtk2_settings + ".bak"):
        shutil.copy(Functions.gtk2_settings,gtk2_settings + ".bak")

    if os.path.isfile(Functions.gtk2_settings):
        with open(Functions.gtk2_settings, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        try:
            data = Functions.check_value(lines, item)
            if not data:
                print("Lines = " + str(len(lines)))
                pos = 4
                print("Pos = " + str(pos))
                lines.insert(pos, ''.join([item,"=\"",str(value),"\"\n"]))
            else:
                pos = int(Functions._get_position(lines, item))
                lines[pos] = ''.join([item,"=\"",str(value),"\"\n"])
    
    
            with open(Functions.gtk2_settings, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox("ERROR!!", "An error has occured getting this setting \'gtk2_save_settings\'")
    

def gtk3_save_settings(value, item):
    if not os.path.isfile(Functions.gtk3_settings + ".bak"):
        Functions.shutil.copy(Functions.gtk3_settings,Functions.gtk3_settings + ".bak")

    if os.path.isfile(Functions.gtk3_settings):
        with open(Functions.gtk3_settings, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            f.close()
        try:
            data = Functions.gtk_check_value(lines, item)
            if not data:
                print("Lines = " + str(len(lines)))
                pos = 4
                print("Pos = " + str(pos))
                lines.insert(pos, ''.join([item,"=",str(value),"\n"]))
            else:
                pos = int(Functions.gtk_get_position(lines, item))
                lines[pos] = ''.join([item,"=",str(value),"\n"])

            with open(Functions.gtk3_settings, 'w') as f:
                f.writelines(lines)
                f.close()
        except:
            Functions.MessageBox("ERROR!!", "An error has occured getting this setting \'gtk3_save_settings\'")

def set_xfce_settings(theme, icon, cursor, cursize):
    if os.path.isfile(Functions.xfce_config):
        try:
            tree = Functions.et.parse(Functions.xfce_config)
            for rank in tree.iter('property'):
                if rank.get("name") == "ThemeName":
                    rank.set("value", str(theme))
                if rank.get("name") == "IconThemeName":
                    rank.set("value", str(icon))
                if rank.get("name") == "CursorThemeName":
                    rank.set("value", str(cursor))
                if rank.get("name") == "CursorThemeSize":
                    rank.set("value", str(cursize))


            tree.write(Functions.xfce_config, encoding="utf-8", xml_declaration=True)
        except:
            Functions.MessageBox("ERROR!!", "An error has occured setting this setting \'set_xfce_settings\'")


def update_index_theme(theme):
    theme_file = "/usr/share/icons/default/index.theme"
    if os.path.isfile(theme_file):
        try:
            with open(theme_file, "r") as f:
                lines = f.readlines()
                f.close()
            for i in range(len(lines)):
                if "Inherits" in lines[i]:
                    lines[i] = "Inherits=" + theme
            
            with open(theme_file, "w") as f:
                f.writelines(lines)
                f.close()
        except:
            pass

def gtk_settings_saved(themeCombo, iconCombo, cursorCombo, cursor_size, fonts):
    # GLib.idle_add(widget.set_sensitive,False)
    gtk3_save_settings(themeCombo, "gtk-theme-name")
    gtk3_save_settings(iconCombo, "gtk-icon-theme-name")
    gtk3_save_settings(cursorCombo, "gtk-cursor-theme-name")
    gtk3_save_settings(int(str(cursor_size).split(".")[0]), "gtk-cursor-theme-size")
    gtk3_save_settings(fonts, "gtk-font-name")
    
    gtk2_save_settings(themeCombo, "gtk-theme-name")
    gtk2_save_settings(iconCombo, "gtk-icon-theme-name")
    gtk2_save_settings(cursorCombo, "gtk-cursor-theme-name")
    gtk2_save_settings(int(str(cursor_size).split(".")[0]), "gtk-cursor-theme-size")
    gtk2_save_settings(fonts, "gtk-font-name")
    
    set_xfce_settings(themeCombo, iconCombo, cursorCombo, int(str(cursor_size).split(".")[0]))
    
    update_index_theme(cursorCombo)
    

    # get_desktop()

    Functions.subprocess.call(["xsetroot -xcf /usr/share/icons/" + cursorCombo + "/cursors/left_ptr " + str(cursor_size)], shell=True)
    
    
    # GLib.idle_add(widget.set_sensitive,True)