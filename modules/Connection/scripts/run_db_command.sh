# Usage: pass in the DB container ID as the argument

# Set database configurations
export CT_DB_USERNAME=connection
export CT_DB_NAME=connection

cat ./db/2020-08-15_init-db.sql | kubectl exec -i $1 -- bash -c "psql -U $CT_DB_USERNAME -d $CT_DB_NAME"
cat ./db/udaconnect_public_location.sql | kubectl exec -i $1 -- bash -c "psql -U $CT_DB_USERNAME -d $CT_DB_NAME"
