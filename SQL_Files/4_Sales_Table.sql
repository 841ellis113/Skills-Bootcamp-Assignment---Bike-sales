CREATE TABLE [dbo].[tblSales](
	[SalesID] [int] IDENTITY(1,1) NOT NULL PRIMARY KEY,
  	[SalesDate] [date],
	[SalesPersonID] [int] FOREIGN KEY REFERENCES tblEmployees (EmployeeID),
	[CustomerID] [int] FOREIGN KEY REFERENCES tblCustomers (CustomerID),
	[ProductID] [int] FOREIGN KEY REFERENCES tblProducts (ProductID),
	[Quantity] [int] 
);