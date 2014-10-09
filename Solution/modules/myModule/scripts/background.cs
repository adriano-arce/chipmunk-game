function createBackground()
{
    %background = new Sprite();

    %background.setBodyType( static );

    %background.Position = "0 0";

    %background.Size = "100 75";

    %background.SceneLayer = 31;

    %background.createEdgeCollisionShape( -50, -37.5, -50, 37.5);
    %background.createEdgeCollisionShape( 50, -37.5, 50, 37.5);
    %background.createEdgeCollisionShape( -50, 37.5, 50, 37.5);
    %background.createEdgeCollisionShape( -50, -34.5, 50, -34.5);

    %background.setDefaultRestitution(0);

    myScene.add(%background);
}