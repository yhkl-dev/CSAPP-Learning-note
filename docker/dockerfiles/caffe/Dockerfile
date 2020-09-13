FROM nvcr.io/nvidia/caffe:19.10-py2

LABEL "version"="0.0.1"
LABEL "maintainer"="yhkl"

COPY boost_1_65_1.tar.gz /workspace/boost_1_65_1.tar.gz 
COPY protobuf-3.2.0.zip  /workspace/protobuf-3.2.0.zip

RUN apt-get update \ 
    && apt-get install gcc-5 g++-5 -y \
    && cd /workspace \
    && unzip protobuf-3.2.0.zip \
    && cd protobuf-3.2.0 \ 
    && sh autogen.sh \ 
    && ./configure \
    && make && make install \
    && cd /workspace && tar xf boost_1_65_1.tar.gz \
    && cd boost_1_65_1 \ 
    && ./bootstrap.sh && ./b2 -j8 --build-dir=/tmp/build-boost --buildtype=complete toolset=gcc stage \
    && echo "export LD_LIBRARY_PATH=/workspace/boost_1_65_1/stage/lib:$LD_LIBRARY_PATH" >> ~/.bashrc \
    && source ~/.bashrc && ldconfig \ 
    && rm -rf /workspace/protobuf-3.2.0,zip  && rm -rf /workspace/boost_1_65_1.tar.gz 
