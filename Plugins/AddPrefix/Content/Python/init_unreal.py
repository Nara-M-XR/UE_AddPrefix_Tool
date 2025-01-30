import unreal
import add_prefix

def main():
    section_name = "mytools"
    section_label = "My Tools"

    #メニューオブジェクトに、セクションを追加する
    ToolMenus = unreal.ToolMenus.get()
    ToolMenu = ToolMenus.find_menu("LevelEditor.MainMenu.Tools")
    ToolMenu.add_section(section_name=section_name,label=section_label,insert_type=unreal.ToolMenuInsertType.DEFAULT,)

    #新しく追加したセクションに追加するエントリーを作成して追加する
    entry = unreal.ToolMenuEntry(name="prefixAuto", type=unreal.MultiBlockType.MENU_ENTRY)
    entry.set_label("Prefix Auto")
    entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "", "add_prefix.selectionContentAutoRename()")
    ToolMenu.add_menu_entry(section_name, entry)

    #新しく追加したセクションに追加するエントリーを作成して追加する
    entry = unreal.ToolMenuEntry(name="prefixInput", type=unreal.MultiBlockType.MENU_ENTRY)
    entry.set_label("Prefix Input")
    entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, "", "add_prefix.addPrefixInputWindow()")
    ToolMenu.add_menu_entry(section_name, entry)

main()
