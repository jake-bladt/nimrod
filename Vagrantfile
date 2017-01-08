# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.synced_folder "F:\\shared_root\\jake\\bulk\\regal\\unsorted\\nimrod", "/mounted/nimrod/"
  config.vm.provision :shell, :path => "provision.sh"
end
