---
title: model security
created: 2025-01-09
updated: 2025-01-09

---

goal:
- Restrict access to Power BI model data with RLS.
- Restrict access to Power BI model objects with OLS.
- Apply good development practices to enforce Power BI model security.

# Restrict access to Power BI model data
- use star schema, bidirectional filter for value.

# define rules 
## Static rules
```dax
'Region'[Region] = "Midwest"
```
## Dynamic rules
```dax
'AppUser'[UserName] = USERPRINCIPALNAME()
```

## Set up role mappings
Role mapping involves assigning Microsoft Entra security objects to roles. Security objects can be user accounts or security groups.
- one should map roles to security groups

## Use single sign-on (SSO) for DirectQuery sources
should be available for non azure sources as well. 
> https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-sso-kerberos-teradata


# Restrict access to Power BI model objects

The feature is available in Power BI Premium to provide backward compatibility for models migrated to Power BI. For this reason, it’s not possible to completely set up OLS in Power BI Desktop.


## Set up OLS
create roles > add ols rules to pbi (not in desktop, but through xmla endpoints, avail in premium)

error message with OLS can be confused for broken report. a better approach might be build separate report.

## Restrictions
- cant mix rls and ols in same role.
- cant set table level security if it breaks relationship chain.
see https://learn.microsoft.com/en-us/analysis-services/tabular-models/object-level-security?view=asallproducts-allversions


# Apply good modeling practices

- define fewer datasets (data models) with well-designed roles.
- create fewer roles by using dynamic rules. A data-driven solution is easier to maintain because you don’t need to add new roles.
- create rules that filter dimension tables, not fact tables. This 
results in faster query performance.
- validate relationships
- Use the `USERPRINCIPALNAME` function instead of `USERNAME` function. 
- validate RLS and OLS by testing all roles.
- Power BI Desktop data source connection USE the SAME credentials used in Power BI service.