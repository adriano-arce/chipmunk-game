function MyModule::create( %this )
{
    exec("./gui/guiProfiles.cs");
    exec("./scripts/scenewindow.cs");
    exec("./scripts/scene.cs");
    exec("./scripts/background.cs");
    exec("./scripts/acorns.cs");
    exec("./scripts/chippy.cs");
    exec("./scripts/controls.cs");

    createSceneWindow();
    createScene();
    mySceneWindow.setScene(myScene);
    createBackground();
    createChippy();
    createacorns(5);
    new ScriptObject(InputManager);
    mySceneWindow.addInputListener(InputManager);
    InputManager.Init_controls();
    myScene.setDebugOff("collision", "position", "aabb");
}

function MyModule::destory ( %this )
{
    shipcontrols.pop();
    InputManager.delete();  
    destroySceneWindow();
}

function InputManager::onTouchDown(%this, %touchId, %worldposition)
{    

//We assign the list of objects that were hit to variable %picked
%picked = myScene.pickPoint(%worldposition);

//%picked.count is the number of items listed in the %picked variable

for(%i=0; %i<%picked.count; %i++)
   {

    //When iterating through the list, getWord will return item number %i in variable %picked

      %myobj = getWord(%picked,%i);

    //If this item belongs to SceneGroup 20, we delete it
      if(%myobj.getSceneGroup() == 20)
      {
      %myobj.safedelete();
      }

   }   
}