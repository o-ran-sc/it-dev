This repo holds various integration and testing development codes.

### Building arm64 version ###
# To build arm64-based version, please use Dockerfile_arm64.
# If there is no specific dockerfile, you can use it on both amd64 and arm64 platforms

docker build -f bldr-imgs/bldr-alpine3/Dockerfile -t bldr-alpine3:12-a3.11 .
docker build -f bldr-imgs/bldr-alpine3-mdclog/Dockerfile -t bldr-alpine3-mdclog:0.0.4 .
docker build -f bldr-imgs/bldr-alpine3-rmr/Dockerfile -t bldr-alpine3-rmr:4.5.2 .
docker build -f bldr-imgs/bldr-ubuntu18-c-go/Dockerfile_arm64 -t bldr-ubuntu18-c-go:1.9.0 .
docker build -f bldr-imgs/bldr-alpine3-go/Dockerfile -t bldr-alpine3-go:2.0.0 .
docker build -f ci/xapp_onboarder/Dockerfile_arm64 -t xapp-onboarder:1.0.7 .

