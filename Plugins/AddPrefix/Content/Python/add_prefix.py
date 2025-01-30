import unreal

def addPrefixInputWindow():
  EAL = unreal.EditorAssetLibrary
  EUS = unreal.get_editor_subsystem(unreal.EditorUtilitySubsystem)
  
  asset = EAL.load_asset('/AddPrefix/EUW_InputWindow_AddPrefix')
  EUS.spawn_and_register_tab(asset)

def selectionContentAddPrefix(prefix):
  EUL = unreal.EditorUtilityLibrary

  selectedAssets = EUL.get_selected_assets() #セレクトしたものを取得 Array

  for asset in selectedAssets:
    prefix_ = prefix + "_"
    asset_name = asset.get_name()
    if prefix_ in asset_name:
      None
    else:
      EUL.rename_asset(asset, "{}{}".format(prefix_, asset_name))

def selectionContentAutoRename():
  #asset_type_dict = {unreal.Material: "M", unreal.MaterialInstance: "MI", unreal.Texture: "T", unreal.Blueprint: "BP", unreal.WidgetBlueprint: "WBP", unreal.NiagaraEmitter: "FXE", unreal.NiagaraSystem: "FXS"}
  asset_type_dict = {"TextureCube": "HDR", \
                    "MaterialInstanceConstant": "MI", \
                    "PhysicsAsset": "PHYS", \
                    "PhysicalMaterial": "PM", \
                    "SkeletalMesh": "SK", \
                    "StaticMesh": "SM", \
                    "Texture2D": "T", \
                    "OpenColorIOConfiguration": "OCIO", \
                    "CurveTable": "CT", \
                    "DataTable": "DT", \
                    "UserDefinedEnum": "E", \
                    "UserDefinedStruct": "F", \
                    "WidgetBlueprint": "WBP", \
                    "EditorUtilityBlueprint": "EUB", \
                    "EditorUtilityWidgetBlueprint": "EUW", \
                    "NiagaraEmitter": "FXE", \
                    "NiagaraSystem": "FXS", \
                    "NiagaraScript": "FXF", \
                    "Rig": "Rig", \
                    "Skeleton": "SKEL", \
                    "AnimMontage": "AM", \
                    "AnimSequence": "AS", \
                    "BlendSpace": "BS", \
                    "DisplayClusterBlueprint": "NDC", \
                    "LevelSequence": "LS", \
                    "MediaSource": "MS", \
                    "MediaOutput": "MO", \
                    "MediaPlayer": "MP", \
                    "MediaProfile": "MPR", \
                    "LevelSnapshot": "SNAP", \
                    "RemoteControlPreset": "RCP"}
  BP_type_dict = {"Actor": "BP", "ActorComponent": "AC", "Interface": "BI"}
  material_type_dict = {0: "M", 4: "PPM"}
  EUL = unreal.EditorUtilityLibrary

  selectedAssets = EUL.get_selected_assets() #セレクトしたものを取得 Array

  for asset in selectedAssets:
    #asset_type = type(asset)
    asset_type = asset.get_class().get_name()

    if asset_type == "Blueprint":
      assetPath = asset.get_path_name().split('.')[0]
      bp = unreal.EditorAssetLibrary.load_blueprint_class(assetPath)
      parent_class = unreal.get_type_from_class(bp)
      parent_class_str = parent_class.__name__

      if parent_class_str in BP_type_dict:
        prefix_ = BP_type_dict[parent_class_str] + "_"
        asset_name = asset.get_name()
        if prefix_ in asset_name:
          None
        else:
          EUL.rename_asset(asset, "{}{}".format(prefix_, asset_name))
    elif asset_type == "Material":

      if asset.material_domain in material_type_dict:
        prefix_ = material_type_dict[asset.material_domain] + "_"
        asset_name = asset.get_name()
        if prefix_ in asset_name:
          None
        else:
          EUL.rename_asset(asset, "{}{}".format(prefix_, asset_name))

    elif asset_type in asset_type_dict:
      prefix_ = asset_type_dict[asset_type] + "_"
      asset_name = asset.get_name()
      
      if prefix_ in asset_name:
        None
      else:
        EUL.rename_asset(asset, "{}{}".format(prefix_, asset_name))
    
    else:
      continue

def checkSelectAssetClass():
  EUL = unreal.EditorUtilityLibrary
  
  selectedAssets = EUL.get_selected_assets() #セレクトしたものを取得 Array
  selectedAssetData = EUL.get_selected_asset_data() #セレクトしたものを取得 Array
  
  for asset in selectedAssets:
    print(f"{asset.get_name()}:{asset.get_class()}")
    print(asset.get_class().get_name())
    

