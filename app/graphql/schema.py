from ariadne import MutationType, QueryType, make_executable_schema
from app.graphql.resolver import resolve_update_order_status

type_defs = """
    type Order {
        id: ID!
        status: String!
    }

    type Mutation {
        updateOrderStatus(id: ID!): Order!
    }

    type Query {
        _: Boolean
    }
"""

query = QueryType()
mutation = MutationType()
mutation.set_field("updateOrderStatus", resolve_update_order_status)

schema = make_executable_schema(type_defs, [query, mutation])
