function createScene()
{
	if ( isObject(myScene))
		destroyScene();

	new Scene(myScene);
}

function destroyScene()
{
	if (!isObject(myScene))
		return;

	createScene();
}