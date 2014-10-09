function createacorns(%Number_of_acorns)
{
    for(%i=0; %i<%Number_of_acorns; %i++)
    {
        %acorn = new Sprite();

        %acorn.setBodyType( dynamic );
        %acorn.Position = getRandom(-20,20) SPC getRandom(-35, 35);
        %acorn.Size = "2 2";
        %acorn.SceneLayer = 1;
        %acorn.createCircleCollisionShape((2*0.85)/2);
        %acorn.SceneGroup = 20;    
        %acorn.Image = "MyModule:Acorn";
        myScene.add(%acorn);
    }
}