# How To Run:

- First step is to setup Kafka, in my case, I used bitnami (helm repo add bitnami https://charts.bitnami.com/bitnami) to generate a values.yaml file that I can use to deploy (helm install udaconnect-kafka -f values.yaml bitnami/kafka
  ), after applying the previously mentioned generated yaml file, you receive further instructions to create a kafka-client / consumer / producer. (To be able to run producer/consumer/topic generating files, you need to access kafka pods bash terminal using kubectl exec --tty -i kafka-release-client --namespace default -- bash)

- After Kafka is setup and running, we can go through remaining services folders and perform 1-2 steps in each folder first step which exists for all services is building,tagging,pushing docker image and deploying service's yaml file using kubectl apply -f (path of yaml file), second step which exists for only some services is running the db seeding scripts using (sh scripts/run_db_command.sh name_of_pod)

After performing above two steps, due to exposed ports in vagrantfile and the forwarded ports in yaml file services, we'd then be able to access all deployed pods locally using localhost:port-of-service, with the frontend port remaining at 30000
