# Usage: pass in the DB container ID as the argument

# Set database configurations
export CT_DB_USERNAME=connection
export CT_DB_NAME=connection

echo "select * from location; " | kubectl exec -i $1 -- bash -c "psql -U $CT_DB_USERNAME -d $CT_DB_NAME"