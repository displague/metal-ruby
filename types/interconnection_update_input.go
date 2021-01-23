// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// InterconnectionUpdateInput interconnection update input
//
// swagger:model InterconnectionUpdateInput
type InterconnectionUpdateInput struct {

	// contact email
	ContactEmail string `json:"contact_email,omitempty"`

	// description
	Description string `json:"description,omitempty"`

	// name
	Name string `json:"name,omitempty"`

	// Updating from 'redundant' to 'primary' will remove a secondary port, while updating from 'primary' to 'redundant' will add one.
	Redundancy string `json:"redundancy,omitempty"`

	// tags
	Tags []string `json:"tags"`
}

// Validate validates this interconnection update input
func (m *InterconnectionUpdateInput) Validate(formats strfmt.Registry) error {
	return nil
}

// MarshalBinary interface implementation
func (m *InterconnectionUpdateInput) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *InterconnectionUpdateInput) UnmarshalBinary(b []byte) error {
	var res InterconnectionUpdateInput
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
