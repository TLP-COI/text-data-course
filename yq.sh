yq ea '
    select(fi==0).dependencies |= . * select(fi==1).dependencies
   |
   (select(fi==0).dependencies[] | select(tag=="!!map"))
   .pip |= . * (select(fi==1).dependencies[]|select(tag=="!!map")).pip
' env.yaml env-deploy.yaml
