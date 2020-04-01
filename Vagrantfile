# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  
  
  config.vm.define "flask1" do |f1|
    f1.vm.provider "docker" do |d|      
        d.image = "my_docker_flask:latest"      
        d.has_ssh = false
        d.create_args = ["--rm", "--hostname", "flask1"]
        d.name = "myflask1"
        d.remains_running = true                
        d.expose = [5000]
    end
  end
  
  config.vm.define "flask2" do |f2|
    f2.vm.provider "docker" do |d2|      
      d2.image = "my_docker_flask:latest"      
      d2.has_ssh = false
      d2.create_args = ["--rm", "--hostname", "flask2"]
      d2.name = "myflask2"
      d2.remains_running = true            
      d2.expose = [5000]
    end
  end

  config.vm.define "nginx" do |f3|
    f3.vm.provider "docker" do |d|      
        d.image = "nginx"      
        d.has_ssh = false
        d.create_args = ["--rm"]
        d.name = "mynginx"
        d.remains_running = true                
        vagrant_root = File.dirname(__FILE__)
        d.volumes = ["#{vagrant_root}/nginx.conf:/etc/nginx/nginx.conf"]
        d.link("myflask1:myflask1")
        d.link("myflask2:myflask2")
        d.ports = ["80:80"]
    end
  end
end
