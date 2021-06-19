scoop install kubectl
;; Use legacy docker for windows
k3d cluster delete k3s-default
k3d cluster create --agents=3 --volume "c:/out:/tmp/out@agent[0,1,2]"
kubectl config use-context k3d-k3s-default
kubectl cluster-info
kubectl create ns argo
kubectl apply -n argo --wait=true -f quick-start-postgres.yml
kubectl rollout status deployment/argo-server -n argo
argo submit -n argo --log argo-gltf-export.yml
;; misc
;; docker run --volume c:/out/:/tmp/out/ -it "nytimes/blender:2.92-cpu-ubuntu18.04" bash