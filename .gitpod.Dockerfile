FROM gitpod/workspace-full-vnc

USER gitpod

RUN sudo apt-get update && sudo apt-get install -y poetry pyside2
