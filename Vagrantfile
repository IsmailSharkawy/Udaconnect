# set up the default terminal
ENV["TERM"]="linux"

# set minimum version for Vagrant
Vagrant.require_version ">= 2.2.10"
Vagrant.configure("2") do |config|
  # Set the image for the vagrant box
  config.vm.box = "centos/7"
  # Set the image version

  # Forward the ports from the guest VM to the local host machine
  # Forward more ports, as needed
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network 'private_network', ip: "192.168.0.200",  virtualbox__intnet: true
  config.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh", disabled: true
  config.vm.network "forwarded_port", guest: 22, host: 2000 # Master Node SSH
  config.vm.network "forwarded_port", guest: 6443, host: 6443 # API Access
  for p in 30000..30100 # expose NodePort IP's
    config.vm.network "forwarded_port", guest: p, host: p, protocol: "tcp"
    end
  # Set the static IP for the vagrant box
  config.vm.network "private_network", ip: "192.168.50.5"
  
  # Configure the parameters for VirtualBox provider
  config.vm.provider "qemu" do |qe|
    qe.arch = "x86_64"
    qe.machine = "q35"
    qe.cpu = "max"
    qe.net_device = "virtio-net-pci"
  end
end
