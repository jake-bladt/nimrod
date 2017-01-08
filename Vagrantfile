# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.synced_folder "C:\\code", "/mounted/code"
  config.vm.synced_folder "C:\\shared_root", "/mounted/cdrive"
  config.vm.synced_folder "E:\\shared_root", "/mounted/edrive"
  config.vm.synced_folder "F:\\shared_root", "/mounted/fdrive"

  config.vm.provision :shell, :path => "provision.sh"

  for i in 8000..8080
    config.vm.network :forwarded_port, guest: i, host: i
  end

end
