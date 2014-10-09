function createSceneWindow()
{
	//Makes sure object doesn't exist
	if (!isObject(mySceneWindow))
	{
		new SceneWindow(mySceneWindow);

		//This is put in by default
		mySceneWindow.Profile = GuiDefaultProfile;

		Canvas.setContent( mySceneWindow );
	}

	//These are defaults
    mySceneWindow.setCameraPosition( 0, 0 );
    mySceneWindow.setCameraSize( 100, 75 );
    mySceneWindow.setCameraZoom( 1 );
    mySceneWindow.setCameraAngle( 0 );
}

function destroySceneWindow()
{
	if ( !isObject(mySceneWindow))
		return;
		
	mySceneWindow.delete();

}