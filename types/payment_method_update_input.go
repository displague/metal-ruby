// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// PaymentMethodUpdateInput payment method update input
//
// swagger:model PaymentMethodUpdateInput
type PaymentMethodUpdateInput struct {

	// billing address
	BillingAddress interface{} `json:"billing_address,omitempty"`

	// cardholder name
	CardholderName string `json:"cardholder_name,omitempty"`

	// default
	Default bool `json:"default,omitempty"`

	// expiration month
	ExpirationMonth string `json:"expiration_month,omitempty"`

	// expiration year
	ExpirationYear int64 `json:"expiration_year,omitempty"`

	// name
	Name string `json:"name,omitempty"`
}

// Validate validates this payment method update input
func (m *PaymentMethodUpdateInput) Validate(formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *PaymentMethodUpdateInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *PaymentMethodUpdateInput) UnmarshalBinary(b []byte) error {
	var res PaymentMethodUpdateInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
